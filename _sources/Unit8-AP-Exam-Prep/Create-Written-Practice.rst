.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Create PT Written Response Practice
===================================

.. raw:: html

	<!-- Copy these 6 lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/Framework2020.js"></script>
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script type="text/javascript" src="assets/lib/vocabulary.js"></script>
	<!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
	<script>
	  $(document).ready(function() {
	    generateSummary(EKmapping['8.11']);
	    generateHovers();
	
	    Tipped.create('.vocab', function(element) {
		var vocab = $(element).data('id');
		return vocabulary[vocab];
	      }, {
	        cache: false,
	          position: 'topleft'
	          });
	  });
	
	 /* var vocabulary = { 
	    "computer":"A computer is a machine that processes information under the control of a program.",
	    "program": "A  computer program is a sequence of instructions that controls the computer.",
	    "hardware": "A computer's hardware includes its electronic and mechanical components that carries out the instructions of a computer program.",
	    "software": "Software consists of the programs that control the computer.",
	    "general purpose computer":"A general purpose computer is one that can run many different programs (e.g. a  smartphone).",
	    "special purpose computer": "A special purpose computer is one that has a fixed program (e.g. a calculator, a watch, a car's brakes).",
	    "RAM":"RAM (Random Access Memory) stores the computer's programs and data temporarily while power is on.",
	    "CPU":"CPU (Central Processing Unit) is that part of the computer's hardware that carries out the instructions of a computer program.",
	    "motherboard":"The motherboard houses the computer's main electronic components.",
	    "chip":"'Chip' is an informal way of describing an integrated circuit (IC) consisting of millions of tiny circuits.", 
	    "machine language": "A machine language is a programming language that is directly readable by the computer’s CPU.",
	    "high level language": "A high level language is a programming language that is human readable (App Inventor) and provides the programmer with easy to understand abstractions.",
	    "compilation": "The process of translating the entire source code into a single binary file.",
	    "interpretation": "The process of translating source code into machine language one instruction at a time and immediately executing instruction.",
	    "byte": "A group of eight binary digits or bits."
	    
	  };
	  */
	
	</script>
	
	
	<h3 id="est-length">Time Estimate: 180 minutes</h3>
	
	<img src="../_static/assets/img/introandgoalsicon.png" width="25" height="25" style="float:left">
	                                                                                                       
Introduction and Goals
----------------------

.. raw:: html
	
	<p></p>
	<table><tbody>
	  <tr><td><iframe src="https://drive.google.com/file/d/1fWruRmW7ldAgJFPNhNC1Nog5DHLMAuUN/preview" allowfullscreen="" width="315" height="420" frameborder="0"></iframe>
	  <br><br></td>
	<td>
	  <p><b><i>The Language Learning Game</i></b>&nbsp;is an educational memory app that allows users to practice learning a different language. The game's code contains all of the programming requirements to satifsy the College Board's Create Performance Task scoring guidelines.&nbsp;&nbsp;</p>
	  <p><b>Objective:</b> In this lesson you will practice answering the Create Performance Task prompts.</p>
	    </td></tr>
	  </tbody></table>
	

Learning Activities
-------------------

.. raw:: html

	<h3>Enhancements </h3>
	<p>Before you can respond to the prompts in the Create Performance Task, you will need to understand how the game works and examine the code that has been provided for you. Complete the enhancement activities to help you get familiar with the code. Remember to work incrementally: implement, test, review, and repeat. You may use <a href="https://docs.google.com/document/d/1RCGzd0OSohNxA5Y5bDARUmUXIAJ-4Uit9UJfwi49NF0/edit" target="_blank" title="">this document</a> to track your progress as you work.<br></p><ol><li>Download the .aia file for The Learning Game.&nbsp;</li><li>Import the file into MIT's App Inventor</li><li>Try playing the game on your device and explore the code.</li><li>Try making these three enhancements:</li><ul><li><span style="white-space: pre;">	</span>Change the app's language to a different language so your app helps you learn to count in that language</li><li><span style="white-space:pre">	</span>Change the initial count of numbers that are spoken to initiate the game.</li><li><span style="white-space:pre">	</span>Try adding a few more numbers to the game</li></ul></ol><ol></ol><ol></ol>
	<p>&lt;&lt;INSERT VIDEO HERE&gt;&gt;</p><br>
	  
	<h3>Create Performance Task Write-up Activity </h3>
	<p>Once you have tried the game and understand the code, answer the AP CSP Create Performance Task prompts.&nbsp;<br></p><ol><li>Review the Create Performance Task prompts in the&nbsp;<a href="https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf" target="_blank" title="">AP CSP Student Directions</a>.&nbsp;</li><li><span class="yui-non">Review the Create Performance Task <a href="https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-2021-create-performance-task-scoring-guidelines.pdf" target="_blank" title="">scoring guidelines</a>.</span></li><li>Make a copy of the submission&nbsp;<a href="https://docs.google.com/document/d/1pgZntXjhm-IO9iHmNA1lMJE7MBDv-sAJOuSaX9LIFsk/copy" target="_blank" title="">document</a>&nbsp;and record your responses.</li></ol><p></p>
	
Summary
-------

.. raw:: html

	<p>In this lesson, you learned how to:</p>
	  <div id="summarylist" class="yui-wk-div">
	  </div>

Self-Check
----------

.. raw:: html

	<h3>Vocabulary</h3>
	
	<p>Here is a table of some of the technical terms you've reviewed in this lesson. Hover over the terms to review the definitions. </p>
	    
	<table align="center">
	<tbody><tr>
	  <td>
	    <span class="hover vocab yui-wk-div" data-id="Input">Input</span>
	    <br><span class="hover vocab yui-wk-div" data-id="Output">Output</span>
	    <br><span class="hover vocab yui-wk-div" data-id="program">Program</span>
	    <br><span class="hover vocab yui-wk-div" data-id="algorithm">Algorithm</span>  
	  </td>
	  
	  <td>
	    <span class="hover vocab yui-wk-div" data-id="comment">Comment</span>
	   <br><span class="hover vocab yui-wk-div" data-id="sequence">Sequence</span>
	  <br><span class="hover vocab yui-wk-div" data-id="selection">Selection</span>
	    <br><span class="hover vocab yui-wk-div" data-id="iteration">Iteration</span>
	  </td>
	  
	  <td>
	   <span class="hover vocab yui-wk-div" data-id="procedural abstraction">Procedural Abstraction</span>
	    <br> <span class="hover vocab yui-wk-div" data-id="parameter">Parameter</span>
	    <br> <span class="hover vocab yui-wk-div" data-id="arguments">Arguments</span>
	    <br> <span class="hover vocab yui-wk-div" data-id="list">List</span>
	  </td>
	  </tr>
	</tbody></table>
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html

	  <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1pgZntXjhm-IO9iHmNA1lMJE7MBDv-sAJOuSaX9LIFsk/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
	
	  <iframe class="portfolioQuestions" style="height:25em" scrolling="no" src="https://docs.google.com/document/d/1pgZntXjhm-IO9iHmNA1lMJE7MBDv-sAJOuSaX9LIFsk/pub"></iframe>
	  
	</div>
