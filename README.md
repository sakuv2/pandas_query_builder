# Pandas Query Builder

## table df
|id| name| age| sex |
|:--|:--|:--|:--|
|1|Rintaro|18|manle|
|2|Mayuri|16|female|
|3|Itaru|18|male|
|4|Chris|18|female|
|5|Moeka|20|female|
|6|Ruka|16|male|
|7|Rumiho|17|female|
|8|Suzuha|18|female|

## SELECT * FROM df WHERE id < 4;
```
Query(df).where("id", "<", 4).get()
```
|id| name| age| sex |
|:--|:--|:--|:--|
|1|Rintaro|18|manle|
|2|Mayuri|16|female|
|3|Itaru|18|male|
|4|Chris|18|female|