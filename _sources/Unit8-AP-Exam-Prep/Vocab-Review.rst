.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

AP CSP Vocabulary Review
========================

.. raw:: html

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
	
	
	<p>To prepare for the AP CSP exam, make sure that you review some vocabulary that you may encounter on the exam. The following <a href="https://quizlet.com/634719872/ap-csp-vocabulary-review-flash-cards/" target="_blank">quizlet</a> consists of all vocabulary from the Mobile CSP course. </p><br>
	<p>
	<iframe src="https://quizlet.com/634719872/match/embed?i=1vnu3c&x=1jj1" height="500" width="100%" style="border:0"></iframe>
	</p>
	
	
Vocabulary
----------
.. raw:: html

	<p>The following table includes all the vocabulary from the Mobile CSP Course. Hover over a word to see the definition and test your knowledge.</p>
	
	<table align="center" id="genTable" border="">
	</table>
