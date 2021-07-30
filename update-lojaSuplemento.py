//Update no MongoDb
use('projeto')
//UpdateOne modificaão de alguns dados 
db.lojaSuplemento.updateOne({qtd: 10},
{
  $set: {valor: 1000, produto: "Creatina"}
}
) 

use('projeto')
//inserão de um dado para testar o UpdateMany
db.lojaSuplemento.insertOne({mercadoria: "Termogênico", "marca": "Probiótica"})


//UpdateMany inserção/modificação de vários dados ao mesmo tempo
use('projeto')
db.lojaSuplemento.updateMany({mercadoria: "Termogênico"},
{$set: {qtd: 90, valor: 4500}
 }
)


//replaceOne redefine o documento, mantendo o id e substituir as informações
db.lojaSuplemento.replaceOne(
  {qtd: 90},
  {mercadoria: "Termogenic", marca: "USS"}
)