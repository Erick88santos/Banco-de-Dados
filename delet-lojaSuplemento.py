use('')
//DeleteOne apagar uma informação
db.lojaSuplemento.deleteOne(
  {mercadoria: ""}
)


//DeleteMany apagar várias informações e até o banco inteiro
use('')
db.lojaSuplemento.deleteMany(
  {mercadoria: ""}
)

//OBS: array vazio, ATENÇÃO!!!
use('')
Apagar todos os registros da coleção!!!!!!
db.lojaSuplemento.deleteMany({})


