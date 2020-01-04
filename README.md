# cli-scraper

```scraper fetch <url>``` - загружает указанный url и выводит результат в stdout

---

```scraper crawl [options]``` - запускает краулер, который собирает ссылки, загружает страницы, извлекает данные и сохраняет результаты в файл

Supported options:
  - ```--format=FORMAT``` or ```-f FORMAT```: формат результирующего файла | {csv, jl}
  - ```--verbosity=VERBOSITY``` or ```-v VERBOSITY```: определяет объем уведомлений и отладочной информации, выводимой во время выполения | {0,1,2}

---