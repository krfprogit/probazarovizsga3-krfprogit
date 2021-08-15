## 3 Feladat: Összeadó

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a összeadó app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html](https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a összeadó app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a két operandust (számot) és az operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban. 

A kalkuláció gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.

Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt. Ennek a kettőnek egyeznie kell.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat3.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(