.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Parity Error Checking optional
==============================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['3.07']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
    
    /*  var vocabulary = { 
        "parity":"In math, parity usually means the fact of being even or odd.",
        "even parity":"In even parity the number of 1s in the sequence add up to an even number.",
        "odd parity":"In odd parity, the number of 1s in the sequence add up to an odd number.",
        "parity bit":"A parity bit is a bit that acts as a check on a set of binary values, calculated in such a way that the number of 1s in the set plus the parity bit should always be even (even parity) or should always be odd (odd parity).",
      };      */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    
    As you learned in the previous lesson, the card "trick" is really not a magic trick at all. It
    is a very precise algorithm of error checking based on the concept of
     <i><b><span class="hover vocab yui-wk-div" data-id='parity'>parity</span></b></i>.
    
    <p>In mathematics, <i><span class="hover vocab yui-wk-div" data-id='parity'>parity</span></i> refers to the evenness or oddness of a number. In
    the card trick, a <i><span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit</i> was added to each row and column such that the 
    additional bit would make the row or column have an even number of 1 bits.  This is 
    known as <i><b>even <span class="hover vocab yui-wk-div" data-id='parity'>parity</span></b></i>.  The "trick" would also work if the <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bits
    were set so as to make each row and column have an odd number of 1 bits.  That would
    be known as <i><b>odd <span class="hover vocab yui-wk-div" data-id='parity'>parity</span></b></i>.
    
    </p><p>It's important to realize that the <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit is not part of the data.  It is <i><b>redundant</b></i>,
    an extra bit, added to the data to allow us to detect if one of the data bits has been flipped
    from its original value.
    
    </p>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Parity Bit Error Detection</h3>
    
    Suppose you are sending a stream of data to a server. By adding
    a <i><span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit</i>, you enable the server to detect some basic
    transmission errors.  For example, if the server expects that every
    byte will contain an <b>even number of 1s</b> and it detects a byte
    such
    as <font color="red">000</font><font color="green">1</font><font color="red">
    0101</font> with an odd number of 1s, it can tell that an error
    occured.  Perhaps the user meant to
    send <font color="red">000</font><font color="green">0</font><font color="red">
    0101</font> but one of the bits was flipped from 0 to 1 during
    transmission.
    
    <p>A <b><span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit</b> is a bit that is added as the leftmost bit of
    a bit string to ensure that the number of bits that are 1 in the bit string
    are <i>even</i> or <i>odd</i>.
    
    </p><p>To see how this works, suppose our data are stored in strings 
    containing 7 bits.  (You might remember that the ASCII scheme, when it 
    was initially introduced, was a 7-bit code.  In practice, a <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit would
    be added to the ASCII code so that 1-bit errors could be detected in
    the resulting 8-bit byte.) 
    
    </p><p>In an <b>even <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> scheme</b> the eighth bit, the <b><span class="hover vocab yui-wk-div" data-id='parity'>parity</span>
    bit</b>, is set to 1 if the number of 1s in the 7 data bits is odd,
    thereby making the number of 1s in the 8-bit byte an even number.  It
    is set to 0 if the number of 1s in the data is even.
    
    </p><p>In an <b>odd <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> scheme</b> the eighth bit, the <b><span class="hover vocab yui-wk-div" data-id='parity'>parity</span>
    bit</b>, is set to 1 if the number of 1s in the 7 data bits is even,
    thereby making the number of 1s in the 8-bit byte an odd number.  It
    is set to 0 if the number of 1s in the data is odd.
    
    </p><p>The following table summarize this approach.
    
    </p><blockquote>
    <table border="1">
    <tbody><tr><th rowspan="2">Data Bits (7)</th><th colspan="2">Add a <span class="hover vocab yui-wk-div" data-id='parity'>parity</span> bit to get 8 bits</th></tr>
    <tr><th>Even <span class="hover vocab yui-wk-div" data-id='Parity'>Parity</span><br/>Total number 1s is even</th><th>Odd <span class="hover vocab yui-wk-div" data-id='Parity'>Parity</span><br/>Total number of 1s is odd</th></tr>
    <tr><td align="center">000 0000  (0 1s)</td><td align="center"><font color="red">0</font>000 0000</td><td align="center"><font color="red">1</font>000 0000</td></tr>
    <tr><td align="center">011 0010  (3 1s)</td><td align="center"><font color="red">1</font>011 0010</td><td align="center"><font color="red">0</font>011 0010</td></tr>
    <tr><td align="center">011 0011  (4 1s)</td><td align="center"><font color="red">0</font>011 0011</td><td align="center"><font color="red">1</font>011 0011</td></tr>
    <tr><td align="center">011 0111  (5 1s)</td><td align="center"><font color="red">1</font>011 0111</td><td align="center"><font color="red">0</font>011 0111</td></tr>
    </tbody></table>
    </blockquote>
    <h3>Parity Exercise</h3>
    <iframe height="550" instanceid="S9xExPRYX0YI" src="https://mobile-csp.org/webapps/parity/ParityExercise.html" title="" width="100%">
    </iframe>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>

Still Curious?
---------------

.. raw:: html

    <p>
    As  you learned in this lesson, with 1 redundant parity bit you can detect 1-bit errors in
    a stream of bits.  Actually, you could detect that an error occurred if 1, 3, 5, or any odd
    number of bits were flipped, but not 2, 4, 6. or any even number of bits.
    
    <p>Detecting an error in a bit stream means that the bit stream would have to be
    retransmitted.  Or, if writing the bit stream to the disk, it would have to be rewritten. 
    
    </p>
    <h4>Error Correction Codes</h4>
    <p>Is it possible to <i>correct</i> errors as well as detect them?  The 
      answer is 'yes' but it will require more, redundant bits. Actually, you saw this
      with the card trick. In that case, each data bit had 2 parity bits, 1 at the end
      of its row and 1 at the end of its column.  That's what enabled us to identify
      the exact bit that was flipped (in the case of a single bit).  And the intersection
      of the row and column that had the wrong parity, is how we identified the bit.  If
      you can identify the bit that was flipped, then you can correct it by flipping it back.
      <br/><br/>
      A more general way of correcting errors such as this is known as <i>Hamming Code</i> and
      the following video shows how this very interesting approach works. 
    
    <br/><br/>
.. youtube:: cBBTWcHkVVY
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/><br/>
    </p>  

Self-Check
-----------

.. raw:: html

    <p>
    
    Here is a table of the technical terms introduced in this lesson. Hover over the terms to review the definitions.
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="parity">parity</span>
    <br/><span class="hover vocab yui-wk-div" data-id="even parity">even parity</span>
    <br/><span class="hover vocab yui-wk-div" data-id="odd parity">odd parity</span>
    <br/><span class="hover vocab yui-wk-div" data-id="parity bit">parity bit</span>
    </td>
    </tr>
    </tbody>
    </table>
    <h3>Parity Questions</h3>
    .. khanex:: khanex3

   		:exercise: parity-error-detection
   		
   	.. khanex:: khanex4
   		:exercise: parity-error-detection-2
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1DSfHurzWXc1RMmFPT2df19Zvoc2R805IseXf2oV3OqY/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTWQIsg8x-3pC7JARMu9-AQ9fNlP6ftc4IunJPmBmDxevvyNaqLTC4HxCC-yV1Zp29KZXOoEcgbbN1X/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Parity Error Checking&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and answer the following questions:&lt;/p&gt;
    
      &lt;ol&gt;
        &lt;li&gt;Explain how the error card trick from Lesson 3.6 uses a parity scheme. Was it an even or odd parity scheme?
        &lt;/li&gt;&lt;li&gt;What are some of the limitations of using parity bits for error detection?
        &lt;/li&gt;&lt;li&gt;Another type of error detection is a check sum. Research what a check sum is and then describe it in your own words. Can a check sum identify where an error occurs?
        &lt;/li&gt;&lt;li&gt;(Optional) Explain in your own words the difference between error detection and error correction. Describe how the error correction process used in the video above allows the computer to fix errors.
        &lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>