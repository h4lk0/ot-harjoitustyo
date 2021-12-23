# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kerrosarkkitehtuuria. Koodin pakkausrakenne on seuraavanlainen:

![architecture_structure](https://user-images.githubusercontent.com/56031728/147282521-9da686cc-1d7a-45ff-a6ec-7e074e820f2e.png)

Pakkaus *ui* sisältää käyttöliittymästä vastaavat luokat. `Entities`-pakkaus sisältää yksittäistä tehtävää kuvaavan luokan ja *database*-pakkaus sisältää tietokantatiedostot, sekä niihin yhteyden muodostavan luokan. Pakkauksesta `services` löytyvät sovelluksen toiminnasta vastaavat luokat.

## Käyttöliittymä
Käyttöliittymä sisältää seuraavat näkymät:
- Aloitusruutu, josta siirrytään tekemään tehtäviä tai muokkaamaan sanalistoja
- Sanalistanäkymä
- Tehtävänäkymä, josta siirrytään tehtävien omiin näkymiin. Nämä näkymät on toteutettu samassa luokassa

Nämä kolme näkymää on toteutettu omina luokkinaan. Näkyvissä voi olla joko aloitusruutu, tehtävänäkymä tai jonkin tietyn tehtävän oma näkymä. Listanäkymä avautuu omaan ikkunaansa.

Näkymien näyttämisestä vastaava koodi on toteutettu [*UI*](../src/ui/ui.py)-luokassa. [*ui*](../src/ui)-pakkaukseen on pyritty toteuttamaan vain graafisesta käyttöliittymästä vastaavaa koodia. Käyttäjältä saatujen syötteiden ja muun tiedon käsittely on pyritty toteuttamaan *services*-pakkauksessa ja yksittäistä tehtäväinstanssia kuvaavassa [*Exercise*](../src/entities/exercise.py)-luokassa.

## Sovelluslogiikka

Sovelluksen keskeisimmän toiminnan muodostavat [*Exercise*](../src/entities/exercise.py)- ja [*Logic*](../src/services/logic.py)-luokat. `Exercise`-luokka kuvaa yksittäistä tehtävää, joka saa uudet vastausta ja vastausvaihtoehtoja kuvaavat muuttujansa `Logic`-luokan kautta. `Exercise`-luokka tarjoaa myös metodin, joka vertaa annettua sanaa sen hetkiseen vastaukseen.

![exercise logic](https://user-images.githubusercontent.com/56031728/147287294-b09b0990-b576-400c-bb7b-3604755e2669.png)

`services`-pakkauksen muut luokat sisältävät tietokantaa ja siihen syötettävää tietoa käsitteleviä toimintoja.

## Tietojen pysyväistalletus

Ohjelman käyttämät sanalistat on tallennettu SQLite-tietokantaan, joka löytyy `database`-pakkauksesta. Tietokannan taulukkojen käsittelystä vastaavat luokan [*DatabaseMethods*](../src/services/database_methods.py) metodit, jotka on toteutettu ulkoisen [*sqlite-utils*](https://sqlite-utils.datasette.io/en/stable/)-kirjaston avulla.

### Taulukoihin lisääminen tiedostosta

Sovellus tarjoaa käyttäjälle mahdollisuuden lisätä taulukkoon kerralla useita rivejä csv-tiedostosta. [*ListFromCSV*](../src/services/csv_handler.py)-luokka vastaa tiedoston sisältämän tiedon muuttamisesta `sqlite-utils`-kirjaston vaatimaan muotoon.

Tiedoston tulee noudattaa samaa formaattia kuin tietokannan taulukot - ***eng, kor***. Sovellus [tarkistaa](../src/services/valid_entry_check.py), että kaikki tiedoston sisältämät merkkijonot ovat oikeassa muodossa ennen niiden lisäämistä taulukkoon. Taulukot käyttävät pääavaimenaan annettuja koreankielisiä sanoja, jonka seurauksena sanan löytyessä jo kohdetaulukosta sovellus päivittää vain sen englanninkielisen käännöksen. Tämä varmistaa, että taulukoihin ei päädy sama sana useasti.

### Tiedostot

Sovelluksen käyttämän tietokantatiedoston nimi on määritelty juuressa sijaitsevassa .env-[konfiguraatiotiedostossa](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/.env). Oletustiedosto on nimeltään `wordlists.db`.

## Päätoiminnallisuudet

Listanäkymä vastaa suurinpiirtein SQL-kyselyjen graafista esitystä, minkä takia en koe tarpeelliseksi kuvata niitä erillisillä sekvenssikaavioilla.

### Tehtävä
Seuraava kaavio kuvaa sovelluksen toimintaa, kun käyttäjä valitsee tehtävätyypin:

![Exercise_diagram](https://user-images.githubusercontent.com/56031728/147293947-8f91fc12-b7a5-4ab8-83ff-32c83da20545.png)

Jokaisen tehtävätyypin graafinen esitys on hieman erilainen, mutta ne kaikki toimivat suurinpiirtein samalla, kaavion kuvaamalla, tavalla. Käyttäjän klikatessa tehtävätyyppiä vastaavaa nappulaa, tapahtumankäsittelijä luo uuden `Exercise`-objektin. `Exercise`-objekti luo uuden `Logic`-objektin ja kutsuu sen metodia `randomize`, joka kutsuu objektin omaa `fetch_wordlist`-metodia, joka hakee `DatabaseMethods`-luokan metodin `get_table` avulla tietokannasta sille annettua merkkijonoa vastaavan nimisen taulukon. `randomize`-metodi arpoo taulukon sisältämästä sanalistasta viisi sanaparia, joista se arpoo vielä yhden oikean vastauksen. Metodi palauttaa nämä muuttujat, jotka käyttöliittymä näyttää käyttäjälle harjoiteltavana sanana ja mahdollisina vastausvaihtoehtoina.

Seuraava kaavio kuvaa vielä sovelluksen toimintaa, kun käyttäjä tarkistaa vastauksensa klikkaamalla `Check`-nappulaa.

![Check_diagram](https://user-images.githubusercontent.com/56031728/147296124-7eef5c31-304e-47fc-a5a2-7cc9b0cefbc1.png)

## Ohjelmaan jääneet heikkoudet

### Sovelluslogiikka

[TableGetter](../src/services/table_getter.py)-luokka käytännössä toistaa `DatabaseMethods`-luokan metodin `get_table`. Metodi erotettiin omaan luokkaansa, jotta koodiin ei muodostuisi riippuvuskehiä, mutta se on todennäköisesti muodostunut turhaksi koodin refaktoroinnin myötä.

Taulukkoon lisättävää tietuetta testaava koodi ei oikeasti tunnista merkkijonojen kieliä vaan tarkistaa pelkästään, että niistä ei löydy kiellettyjä merkkejä. Käytännössä siis `eng_is_valid`-metodi päästää läpi minkä tahansa englannin aakkosista koostuvan merkkijonon, esimerkiksi `glxblt`. Vastaavasti `kor_is_valid` päästää läpi myös muut merkkijonot, jotka koostuvat muista kuin latinalaisista kirjaimista. Sanan tunnistaminen oikeaksi kohdekielen sanaksi vaatisi omat kielentunnistukseen tarkoitetut kirjastonsa.

### Käyttöliittymä

Käyttöliittymään on jääny jonkin verran toisteisuutta esimerkiksi eri tehtävätyyppien näkymien välillä. Lisäksi jotkin graafiset komponentit voisi toteuttaa fiksummin.
