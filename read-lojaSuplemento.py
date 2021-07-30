use('projeto')
//Read/select * from lojaSulmento
db.lojaSuplemento.find()



use('projeto')
//Read/select 8 from lojaSuplemento where qtd = 10 
db.lojaSuplemento.find({"qtd": 10})


use('projeto')
//Read/select8 from lojaSuplemento where qtd = 10 sem aparecer o id
db.lojaSuplemento.find({"qtd": 10},{"_id":0})



use('projeto')
//Read/select 8 from lojaSuplemento where mercadoria = Probiótica
db.lojaSuplemento.find({"qtd": 20})


use('projeto')
//Read/select 8 from lojaSuplemento where qtd =  Probiótica sem aparecer o id
db.lojaSuplemento.find({"qtd": 20},{"_id":0})




use('projeto')
// Read/select * estoque que contenha 10 produtos no mínimo e no máximo 20 = todos
db.lojaSuplemento.find({qtd:{$gte: 10, $lte: 30}})




use('projeto')
// ordenação por valor menor até maior
db.lojaSuplemento.find({mercadoria: 'Whey protein'}).sort({"valor":1})




use('projeto')
// ordenação por valor do maior até o valor menor
db.lojaSuplemento.find({mercadoria: 'Whey protein'}).sort({"valor":-1})