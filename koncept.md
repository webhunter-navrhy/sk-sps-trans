# Peter Suja – SPS Trans (dokončovacie práce, Bratislava): koncept

## Tri koncepty
1. **Vzorkovník** – web ako vzorkovnica materiálov z predajne obkladov: každá služba je jedna „vzorka“ (obklad, drevo, omietka, sadrokartón) s kartičkou ako v showroome; úvod je vejár vzoriek vedľa hotovej miestnosti.
2. **Súpis prác po miestnostiach** – kúpeľňa / kuchyňa / izba ako záložky, zákazník si odškrtá práce a vznikne súpis pre dopyt.
3. **Od hrubej stavby po kľúč** – scroll od holého muriva k hotovej miestnosti (vrstvy povrchov).

## Výber: 1. Vzorkovník
Dokončovacie práce sú o povrchoch, ktoré zákazník vyberá v predajni podľa vzoriek; kartička vzorky (názov, materiál, kde sa hodí) je jazyk, ktorý pozná. Koncept unesie aj chýbajúce vlastné fotky: textúry materiálov sú pravdivé ako ilustrácia a neklamú o realizáciách. Koncept 2 by opakoval interaktívny protokol z HaK (predchádzajúci web v registri), koncept 3 je blízko „rezu domom“ (FERO.bau, Tref).

## Skladba sekcií
1. Hlavička: názov textom (logo nemá), menu Služby / Dopyt / Kontakt, telefón.
2. Úvod: h1 „Dokončovacie práce v Bratislave“, perex, vpravo hotová miestnosť + vejár 4 vzoriek (obklad, drevo, omietka, sadrokartón) s kartičkami.
3. **Signature: Vzorkovník služieb** – 5 vzoriek pod sebou, každá: veľká textúra materiálu + fotka priestoru + kartička (názov, čo zahŕňa, kde sa hodí). Striedanie strán.
4. Pás „Okrem toho“: prípravné práce a preprava do 3,5 t (doklad: živnosti, názov SPS Trans) – typograficky, bez fotky.
5. Dopyt: miestnosť (čipy), práce (čipy), približná plocha, fotka miestnosti, kontakt. Vedľa krátko „čo nám pošlite“.
6. Kontakt + pätička s IČO.

Signature moment: vzorkovník (kartičky vzoriek), na úvode vejár, ktorý sa pri scrolle jemne rozloží (CSS scroll-driven, s reduced-motion vypnuté).

## Písmo, paleta, fotky
- Young Serif 400 (display, bez kurzívy – nepoužívame) + Public Sans 300–600 (text, kartičky). Pevný serif pre remeslo podľa typografie.md.
- Paleta: omietka #f2eee7, papier kartičky #fbf9f5, grafit #23211e, škára #c9c1b4, terakota #a9502e (jediný akcent, z dlažby). Svetlý editoriál.
- Fotky ilustračné (Unsplash), textúry + 4 priestory; jednotná teplá gradácia, mierne stlmené.

## Zakázané vzory
- Číslovanie vzoriek „vzorka č. 1–5“: ÁNO, ale ako katalógové číslo vzorky na kartičke (koncept), nie obrysové 01/02 číslice. (1 vzor s odôvodnením)
- Marquee, zrno, tmavé štatistiky, scroll indikátor, polaroidy, pilulková navigácia, mono nadtitulky: nie.

## Porovnanie
- Posledné SK weby: HaK (protokol, Schibsted Grotesk), BTN, Tref (Newsreader), Fenima/Zener/FERO.bau/Gora/Comba (Instrument Serif). Young Serif + Public Sans sa neopakujú, skladba „vzorkovník“ tiež nie.
- Odmietnuté: žiadny tmavý luxus, žiadne „obdĺžničky“ bez nápadu – kartičky sú obsah (materiál, použitie), nie dekor.
