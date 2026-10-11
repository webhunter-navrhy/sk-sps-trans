// Peter Suja – SPS Trans: menu, odhaľovanie vzoriek, dopyt (v návrhu sa nič neodosiela).
document.documentElement.classList.add('js');

(function () {
  // menu na mobile
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var o = menu.classList.toggle('otvorene');
      burger.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { menu.classList.remove('otvorene'); burger.setAttribute('aria-expanded', 'false'); }
    });
  }

  // odhaľovanie pri scrolle
  var ciele = document.querySelectorAll('.vzorka, .okrem-p');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (zaznamy) {
      zaznamy.forEach(function (z) { if (z.isIntersecting) { z.target.classList.add('je'); io.unobserve(z.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    ciele.forEach(function (el) { el.classList.add('odhal'); io.observe(el); });
  }

  // názov vybranej fotky
  document.querySelectorAll('.subor-tl input').forEach(function (i) {
    i.addEventListener('change', function () {
      var m = i.parentNode.querySelector('.subor-meno');
      m.textContent = i.files.length ? (i.files.length > 1 ? i.files.length + ' fotky vybrané' : i.files[0].name) : m.getAttribute('data-prazdne');
    });
  });

  // dopyt: kontrola povinných volieb, v návrhu sa nič neodosiela
  var form = document.getElementById('formular');
  if (!form) return;
  var stav = form.querySelector('.formular-stav');
  form.addEventListener('change', function () {
    form.querySelectorAll('.volby.chyba').forEach(function (f) { if (f.querySelector('input:checked')) f.classList.remove('chyba'); });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (form.querySelector('.past input').value) return;
    var chyby = [], prve = null;
    form.querySelectorAll('.volby[data-povinne]').forEach(function (f) {
      if (!f.querySelector('input:checked')) { f.classList.add('chyba'); chyby.push(f.querySelector('legend').textContent.replace('?', '').toLowerCase()); prve = prve || f; }
    });
    ['meno', 'kontakt'].forEach(function (n) {
      var i = form.elements[n];
      if (!i.value.trim()) { chyby.push(n === 'meno' ? 'meno' : 'telefón alebo e-mail'); prve = prve || i; }
    });
    if (chyby.length) {
      stav.textContent = 'Ešte doplňte: ' + chyby.join(', ') + '.';
      (prve.tagName === 'FIELDSET' ? prve.querySelector('input') : prve).focus();
      return;
    }
    var endpoint = form.getAttribute('data-endpoint');
    if (form.getAttribute('data-demo') === '1' || !endpoint) {
      stav.textContent = 'Toto je ukážka webu, dopyt sa neodoslal. Po spustení Vám budú dopyty chodiť priamo na e-mail.';
      return;
    }
    stav.textContent = 'Odosielam…';
    fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); stav.textContent = 'Ďakujeme, dopyt sme dostali. Ozveme sa Vám.'; })
      .catch(function () { stav.textContent = 'Odoslanie sa nepodarilo. Napíšte nám prosím e-mail.'; });
  });
})();
