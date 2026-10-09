# Kako računala igraju šah? — jednostavan predložak

Jedan stupac teksta, navigacija na vrhu, obični naslovi i poveznice.
Izgled slijedi referencu lunitur.github.io/nixos-seminar/, uz stalnu tamnu temu.
Bez JavaScripta, vanjskih fontova, instalacije i kompiliranja.

## Otvaranje i uređivanje

Raspakiraj ZIP i otvori index.html u pregledniku:

```bash
xdg-open index.html
```

- index.html: sav sadržaj. Uredi u Codiumu ili drugom tekstualnom editoru.
- assets/style.css: boje, širina teksta i veličine fontova.
- materijali/: tvoj PDF, slike i prateće datoteke.
- kod/: tvoja samostalna implementacija za seminar.
- PROVJERA.md: obveze i kontrolni popis.

Zamijeni odlomke u uglatim zagradama vlastitim tekstom. To nisu dijelovi
napisanog rada. Ukloni upute i oznaku predloška kada je rad gotov.
Uredi ime, naslov i datum. Poglavlja slobodno mijenjaj; ažuriraj i sadržaj.
Izjavu o AI-ju dopuni prema stvarnoj uporabi alata.

## Dodavanje PDF-a

Kopiraj PDF iz TeXstudija u materijali/seminar.pdf. U odjeljku Prezentacija
zamijeni odlomak o nedodanom PDF-u s:

```html
<p><a href="materijali/seminar.pdf">Preuzmi prezentaciju (PDF)</a></p>
```

Poveznica iz navigacije zasad vodi do tog odjeljka. Ako želiš izravno
otvaranje PDF-a kao na referentnoj stranici, promijeni njezin href na
materijali/seminar.pdf nakon što dodaš datoteku.

## Kod, zadaci i literatura

Vlastiti kod dodaj u kod/ pa u index.html upiši poveznicu na mapu u svojem
GitHub repozitoriju. Napiši upute za pokretanje i primjere ulaza/izlaza.

Objavi jedan do tri vlastita zadatka tijekom ili odmah nakon izlaganja.
Upiši način i rok predaje. Stranica nema obrazac ni sustav predaje odgovora.
Neobjavljena rješenja nemoj spremati u javni repozitorij ni HTML komentare.

Zamijeni bibliografska mjesta provjerenim izvorima. Iz teksta možeš
povezivati na njih ovako: <a href="#izvor-1">[1]</a>.

## Slike i formule

```html
<figure>
  <img src="materijali/dijagram.svg" alt="Opis vlastitog dijagrama">
  <figcaption>Opis i izvor.</figcaption>
</figure>
```

Renderer LaTeX formula nije uključen. Formule pripremi kao SVG s tekstualnim
opisom ili naknadno uključi MathJax/KaTeX. Sam LaTeX između dolara nije dovoljan.
HTML oznake unutar prikazanog koda escapeaj: znak < kao &lt; i & kao &amp;.

## GitHub Pages

1. Napravi javni repozitorij sah-seminar.
2. Prenesi sadržaj ove mape u korijen repozitorija, uključujući assets/.
   index.html mora biti u korijenu, ne u dodatnoj mapi sah-seminar/.
3. Settings → Pages → Deploy from a branch → main → /(root) → Save.
4. Stranica će biti na https://TVOJE-IME.github.io/sah-seminar/.

Za osobnu početnu stranicu nazovi repozitorij TVOJE-IME.github.io.
Sve lokalne poveznice relativne su i rade pod putanjom projekta.

## Pravila kolegija

Ovo je struktura i kod web-stranice, ne dovršeni seminarski rad.
Tekst, matematiku i seminarsku implementaciju napiši samostalno.
Provjeri minimalne zahtjeve koji nisu brojčano navedeni u dostavljenim uputama.
Najkasnije 24 sata prije izlaganja objavi barem tekst i kod.
Planiraj ukupno oko 45 minuta, uključujući 5–10 minuta diskusije.
