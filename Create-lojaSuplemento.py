//inserindo dados via mongo DB Playground
//selecionar o database a ser utilizado
use('projeto')

//EX: insert com o insertOne
db.lojaSuplemento.insertOne({
"mercadoria": "Whey protein",
"qtd": 10,
"marca": "Integralmédica",
"valor": 1000
})

//EX: insert com o insertMany
db.lojaSuplemento.insertMany(
  [
    {"mercadoria": "Creatina", "qtd": 10, "marca": "Integralmédica", "valor": 1500 },
    {"mercadoria": "BCAAs", "qtd": 10, "marca": "Integralmédica", "valor": 500 },
    {"mercadoria": "Whey protein", "qtd": 20, "marca":"Probiótica", "valor": 2000 },
    {"mercadoria": "Creatina", "qtd": 20, "marca":"Probiótica", "valor": 3000 },
    {"mercadoria": "BCAAs", "qtd": 20, "marca":"Probiótica", "valor": 1000 },
    {"mercadoria": "Whey protein", "qtd": 30, "marca": "BodyAction", "valor": 2100 },
    {"mercadoria": "Creatina", "qtd": 30, "marca": "BodyAction", "valor": 3000 },
    {"mercadoria": "BCAAs", "qtd": 30, "marca": "BodyAction", "valor": 750 }	
  ]
)

