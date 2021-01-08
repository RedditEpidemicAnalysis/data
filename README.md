# Reddit Analysis on COVID-19

![PowerShell](https://img.shields.io/badge/PowerShell-5.1.x-blue.svg)
![CC0 license](https://img.shields.io/badge/License-CC0-green.svg)

Below can be found a list of data retrieval scripts that help make this work possible.
The pathing can be changed to any desired location.

1. Open an _ADMIN_ PowerShell window install the CLI tools.
   ```{ps1}
   pip install psaw
   pip install python-dateutil
   ```
2. Open a PowerShell window
   ```{ps1}
   $months = @(
      '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08',
      '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02')
   for($i = 0; $i -lt ($months.length -1); $i++) {
      psaw `
         -s COVID19positive `
         -l 1000000 `
         --format json `
         --after "$($months[$i])-01" `
         --before "$($months[$i+1])-01" `
         -f id,created_utc,author,score,num_comments,title,selftext `
         -o "d:/datasets/reddit/submissions.$($months[$i]).json" `
         --prettify --verbose `
         submissions
      Start-Sleep -s 60
   }
   ```
 
# Citation

If you use the dataset in academic work, please consider citing it based on the original source.
All the `.tar.gz`s in [Releases](https://github.com/RedditEpidemicAnalysis/data/releases) are a cache of a cache.

```{bib}
@misc{baumgartner2021,
  title={Historical submissions from /r/COVID19positive},
  author={Jason Baumgartner},
  year={2021},
  publisher={pushshift.io},
  url={https://pushshift.io/},
  urldate={2021-01-07}
}
@misc{marx2021python,
  title={Python Pushshift.io API Wrapper},
  author={David Marx},
  year={2021},
  url={https://github.com/dmarx/psaw},
  urldate={2021-01-07}
}
```
