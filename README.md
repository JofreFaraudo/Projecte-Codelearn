# Projecte Codelearn
## llista de coses per a fer:
* Crear un app simple que servirà per a conectar-se amb el server.
* Crear la base de dades.
* Fer que la aplicació es comuniqui amb la base de dades i et mostri una llista de que hi ha.
* Fer que puguis marcar cada element com a fet per separar
* Afegir que puguis afergir coses al server
* Mirar de fer una app web que faci el mateix
## API:

Coses que ha de tenir la API
* Crear un TODO
* Eliminar un TODO
* Marcar un TODO com a fet
* Llistar els TODOs

### Crear TODO
`POST /todo/new`

Payload
`
{
	"done": true|false,
	"name": string
}
`

Return
`
{
	"id": num
}
`

### Eliminar TODO
`DELETE /todo`

Payload
`
{
	"id": num
}
`

Return
`
{
	"status": Error|Ok
}
`
### Editar TODO 
`UPDATE /todo/`

Payload
`
{
	"id": num,
	"name": OPTIONAL string,
	"state": OPTIONAL checked|unchecked

}
`

Return
`
{
	"status": Error|Ok
}
`

### llistar TODO 
`GET /todo`

Return
`
{
	"todos": [
		{
			"id": num,
			"state": bool,
			"name": string
		}
	]
}
`
