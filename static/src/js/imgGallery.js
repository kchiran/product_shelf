$(document).ready(function(){
  $( ".gallery" ).click(function(event) {
	$(this).toggleClass( "choose" );
	//prev_val = $("#textBox1").val()
    prev_val = $("#textBox1").val()
				//if (prev_val==null){
					if(prev_val.includes($( this ).attr("id")+";")){
						prev_val = prev_val.replace($( this ).attr("id")+";","")
						$("#textBox1").val(prev_val)
					}
					else
						$("#textBox1").val($("#textBox1").val() + $( this ).attr("id")+";")
  });
 
});