# 1 Feladat: Keressük a téglalap kerületét

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a téglalap kerülete app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/x234.html](https://black-moss-0a0440e03.azurestaticapps.net/x234.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

* Helyes kitöltés esete:
    * a: 99
    * b: 12
    * Eredmény: 222

* Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 12
    * Eredmény: NaN

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN   

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `x234.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(