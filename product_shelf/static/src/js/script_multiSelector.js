$(document).ready(function()
{
	$(".drag").click(function(e)
	{
		var t = $(".drag");
		console.log("first click " + t.index(this))
		var lowEnd = t.index(this);
		console.log("ff " + $(this).attr("id"))
		var shiftHeld = false;
		$('.drag').on('mousedown', function(e) 
		{	
			shiftHeld = e.ShiftKey
			//e.preventDefault()
			console.log("second click "+t.index(this))
			//find the index of selector after shift
			var u = $(".drag");
			var highEnd = u.index(this);
			var list = [];
			var v = $(".drag");
			//Compare selector indices, and loop from lower to higher
			if (highEnd > lowEnd){
					for (var i = (lowEnd+1); i < highEnd; i++){
					//j=i+1;
					list.push(i);
					
					v.eq((i)).toggleClass("selected")
					console.log("aaa + " + v.eq(i).attr("id"))
					prev_val = $("#fieldid").val()
					if(prev_val.includes(v.eq(i).attr("id")+";")){
						prev_val = prev_val.replace(v.eq(i).attr("id")+";","")
						$("#fieldid").val(prev_val)
					}
					else
						$("#fieldid").val($("#fieldid").val() + v.eq(i).attr("id")+";")
				}
			}
			else{
					for (var i =lowEnd; i > highEnd; i--) {
						v.eq(i).toggleClass("selected")
					list.push(i);
					console.log("aaa + " + v.eq(i).attr("id"))
					prev_val = $("#fieldid").val()
					if(prev_val.includes(v.eq(i).attr("id")+";")){
						prev_val = prev_val.replace(v.eq(i).attr("id")+";","")
						$("#fieldid").val(prev_val)
					}
					else
						$("#fieldid").val($("#fieldid").val() + v.eq(i).attr("id")+";")
				}
			}
			console.log(list);
		} );
	});
});