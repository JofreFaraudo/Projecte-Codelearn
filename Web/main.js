$.ajax({method:'GET',url:"http://dziban.net:5000/todo"}).done(function(data){
	console.log(data);
	let todos = data.todos;
	if(todos == undefined) return;
	for(let i=0;i < todos.length; ++i){
		var actual = todos[i];
		$((actual['state']==0?'#todos-no-fets':'#todos-fets')).append("<tr><td contenteditable='false' id='"+actual['id']+"'>"+actual['name']+
			"</td><td><button class='delete' todo-id='"+actual['id']+"'>Esborrar</button>" +
			"<button class='edit' todo-id='"+actual['id']+"'>Editar</button>" +
			"<button class='"+(actual['state']==0?'marcarcomafet':'desmarcarcomafet')+"' todo-id='"+actual['id']+"'>"+(actual['state']==0?'Marcar com a fet':'Desmarcar com a fet')+"</button></tr>");
	}
	updateButtons();
});

function updateButtons() {
	$(".marcarcomafet").unbind("click");
	$(".marcarcomafet").each(function(i, o) {
		$(o).click(function(e){
			var id_todo = $(e.currentTarget).attr("todo-id");
			$.ajax({method:'PUT',
				url:'http://dziban.net:5000/todo',
				contentType: 'application/json',
				data: JSON.stringify({"id":id_todo,"state":1})})
			.done(function(){
				window.location.reload();
			})
		})
	});

	$(".desmarcarcomafet").unbind("click");
	$(".desmarcarcomafet").each(function(i, o) {
		$(o).click(function(e){
			var id_todo = $(e.currentTarget).attr("todo-id");
			$.ajax({method:'PUT',
				url:'http://dziban.net:5000/todo',
				contentType: 'application/json',
				data: JSON.stringify({"id":id_todo,"state":0})})
			.done(function(){
				window.location.reload();
			})
		})
	});

	$(".delete").unbind("click");
	$(".delete").each(function(i, o) {
		console.log(o);
		$(o).click(function(e){
			var id_todo = $(e.currentTarget).attr("todo-id");
			$.ajax({method:'DELETE',
				url:'http://dziban.net:5000/todo',
				contentType: 'application/json',
				data: JSON.stringify({"id":id_todo})})
			.done(function(){
				window.location.reload();
			})
		})
	});

	$(".edit").unbind("click");
	$(".edit").each(function(i, o) {
		console.log(o);
		$(o).click(function(e){
			var id_todo = $(e.currentTarget).attr("todo-id");
			$("#"+id_todo).attr("contenteditable","true");
			$("#"+id_todo).focus();
			$(o).text("Desar");
			$(o).addClass("save");
			$(o).removeClass("edit");
			updateButtons();
		})
	});

	$(".save").unbind("click");
	$(".save").each(function(i, o) {
		console.log(o);
		$(o).click(function(e){
			var id_todo = $(e.currentTarget).attr("todo-id");
			$.ajax({method:'PUT',
				url:'http://dziban.net:5000/todo',
				contentType: 'application/json',
				data: JSON.stringify({"name":$("#"+id_todo).html(),"id":id_todo})
			})
			.done(function(){
				window.location.reload();
			})
		})
	});

	$("#submit").unbind("click");
	$("#submit").click(function(){
		let name = $("#name").val();
		console.log(name);
		$.ajax({method:'POST',
				url:'http://dziban.net:5000/todo',
				contentType: 'application/json',
				data: JSON.stringify({"name":name})
			})
			.done(function(){
				window.location.reload();
			})
	})
}

updateButtons();
