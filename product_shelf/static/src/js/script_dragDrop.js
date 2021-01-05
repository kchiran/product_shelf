$(document).ready(function(){
	$(".drag").click(function(e){
		if (e.ctrlKey) {
			//e.preventDefault();
			prev_val = $("#fieldid").val()
				//if (prev_val==null){
					if(prev_val.includes($( this ).attr("id")+";")){
						prev_val = prev_val.replace($( this ).attr("id")+";","")
						$("#fieldid").val(prev_val)
					}
					else
						$("#fieldid").val($("#fieldid").val() + $( this ).attr("id")+";")
				//}
		}
	}).draggable({
		helper: "clone", 
		drag : function(event, ui){
			console.log("element : " + $(this))
			prev_val = $("#fieldid").val()
			/*if(prev_val.includes($( this ).attr("id")+";")){
				prev_val = prev_val.replace($( this ).attr("id")+";","")
				$("#fieldid").val(prev_val)
			}
			else
				$("#fieldid").val($("#fieldid").val() + $( this ).attr("id")+";")*/
		}
	});

	var helper = $( ".drag " ).draggable( "option", "helper" );
	
    $( ".droppable" ).droppable({
      drop: function( event, ui ) {
		console.log($( this ).first())
		console.log("Source " + $("#fieldid").val())
		console.log("Dest1 " +  $( this ))
		console.log("Dest " +  $( this ).parent($("a")).attr("id"))
		$( this ).first().css( "background-color", "#63C5DA" );
		var source = $("#fieldid").val();
		var dest = $( this ).parent($("a")).attr("id");
		location.href="/pcm/update/"+source+"/"+dest;
		}
	});
});