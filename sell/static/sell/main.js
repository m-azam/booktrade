$(document).ready(function(){
		$("#mb").click(function () {
			$("#dlist").slideToggle("slow");
		});
		$(".desky").css("visibility","hidden");
		$(".mobbi").css("visibility","hidden");
		$("#card").flip({
    		trigger: 'manual'
		});
		$("#card1").flip({
    		trigger: 'manual'
		});
		$('.mfb').click(function() {
    		$('#card').flip(true);
    		$(".mobbi").css("visibility","visible");
		});
		$('.dfb').click(function() {
    		$('#card1').flip(true);
    		$(".desky").css("visibility","visible");
		});
		$(".selectmenu").selectmenu();
   		var max_fields= 10;
    	var add_button=$(".add_book");
  
    	var x = 1;
    	$(add_button).click(function(e){
        	e.preventDefault();
        	if(x < max_fields){
            	x++;
           		$(".inner_book_div").append('</br><label for="Subject'+x+'" class="lblp2">Subject</label>&nbsp;<input type="text" name="subject'+x+'">&nbsp;<label for="bookname'+x+'" class="lblp2">Book Name</label>&nbsp;<input type="text" name="bookname'+x+'">&nbsp;<label for="price'+x+'" class="lblp2">Price</label>&nbsp;<input type="text" name="price'+x+'"><hr>');
        	}
  			else
  			{
  				alert('You can only post 10 books at once.');
  			}
   		});
});







