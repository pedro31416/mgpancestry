# mgpancestry

Scraping Mathematical Genealogy Project for a scholar's ancestry. This project is inspired from [mgptree](https://github.com/gnstanley/mgptree), which scraps the Mathematical Genealogy Project for a scholar's descendence.

Uses [scrapy](http://scrapy.org/) and python (2.7.10, in case a bug is found).

To run, clone this directory and run

```
scrapy crawl mgpspider -a root=202169 -o output.json
```

where output.json is a stand-in for the [output file](http://doc.scrapy.org/en/latest/topics/feed-exports.html?highlight=output) and [202169](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=202169) is a stand-in for the id of the mathematician at the root of the tree to crawl from.

Please respect the [`robots.txt`](https://genealogy.math.ndsu.nodak.edu/robots.txt) file for the Mathematical Genealogy Project when using this web scraper.