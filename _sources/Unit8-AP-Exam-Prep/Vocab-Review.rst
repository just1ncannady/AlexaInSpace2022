.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

AP CSP Vocabulary Review
========================

.. raw:: html

	<!-- Copy these 6 lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/framework.js"></script>
	<!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
	<link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script type="text/javascript" src="assets/lib/vocabulary.js"></script>
	<script>
	$(document).ready(function() {
	  // FIRST GENERATE VOCAB TABLE, then add hover
	    generateVocabTable();
	  Tipped.create('.vocab', function(element) {
	var vocab = $(element).data('id');
	return vocabulary[vocab];
	    }, {
	      cache: false,
	        position: 'topleft'
	        });
	});
	
	function generateVocabTable()
	{
	var table = document.getElementById('genTable');
	var words = Object.keys(vocabulary).sort();
	var numWords = words.length;
	var columns = 4;
	var wordsPerColumn = numWords/4;
	
	// populate table
	for(r = 0; r < wordsPerColumn ; r++) 
	{		
	    var row = table.insertRow(r);		
	    for(c = 0; c < columns; c++)
	  {			
	   var cell = row.insertCell(c);
	      var word = words[(r * columns) + c];
	      if (word != undefined)  
	          cell.innerHTML = "<span class='hover vocab yui-wk-div' data-id='" + word + "'>" + word + "</span>";
	    }
	}    
	}
	</script>
	
	
	To prepare for the AP CSP exam, make sure that you review some vocabulary that you may encounter on the exam. The following <a href="https://quizlet.com/422489030/ap-csp-vocabulary-review-flash-cards/" target="_blank">quizlet</a> consists of all vocabulary from the Mobile CSP course. <br>
	
	<iframe src="https://quizlet.com/422489030/match/embed?i=1vnu3c&x=1jj1" height="500" width="100%" style="border:0"></iframe>
	
	
	
Vocabulary
----------

	<p>The following table includes all the vocabulary from the Mobile CSP Course. Hover over a word to see the definition and test your knowledge.</p>
	
	<table align="center" id="genTable" border="">
	</table>
