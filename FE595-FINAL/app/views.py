
from app import app
from flask import render_template, request
from .forms import InputTextForm
from .nlp import TextAnalyser
from textblob import TextBlob, Word
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob.sentiments import NaiveBayesAnalyzer

    # Submit button in web for pressed
@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def manageRequest():

      # some useful initialisation
    print('--->','TR'  in request.form.values())
    theInputForm = InputTextForm()
    userText = "and not leave this empty!"
    typeText = "You should write something ..."
    language = "EN"
    language = request.form['lang'] # which language?
    

      # POST - retrieve all user submitted data
    if theInputForm.validate_on_submit():
        userText = theInputForm.inputText.data
        typeText = "Your own text"
        

    # DEBUG flash('read:  %s' % typeText)

    stemmingEnabled = request.form.get("stemming")
    stemmingType = TextAnalyser.NO_STEMMING

    if stemmingEnabled:
        if request.form.get("engine"):
            stemmingType = TextAnalyser.STEM
        else:
            stemmingType = TextAnalyser.LEMMA
    else:
        stemmingType = TextAnalyser.NO_STEMMING


    #flash('read:  %s' % stemmingEnabled)


          # Which kind of user action ?
    if 'TR'  in request.form.values():
        print("888888888888888")
        
        blob = TextBlob(userText, analyzer=NaiveBayesAnalyzer())
    
    
    
        translate_to = language
        print("translate_response:--------->",translate_to)
    
        print(blob, translate_to)
        if (translate_to.lower() == 'french'):    
            resp = str(blob.translate(to='fr'))                     
        elif (translate_to.lower() == 'telugu'):
            resp = str(blob.translate(to='te'))                  
        elif (translate_to.lower() == 'hindi'):
            resp = str(blob.translate(to='hi'))
        elif (translate_to.lower() == 'german'):
            resp = str(blob.translate(to='de'))
        elif (translate_to.lower() == 'greek'):
            resp = str(blob.translate(to='el'))
        elif (translate_to.lower() == 'spanish'):
            resp = str(blob.translate(to='es'))
            
                  
        return render_template('translation_results.html',
                           title='Translation',                           
                           translation=resp)
    
        
    elif 'BA'  in request.form.values():
            # GO Text Analysis

        print("------------")
        myText = TextAnalyser(userText, language) # new object

        myText.preprocessText(lowercase = theInputForm.ignoreCase.data,
                              removeStopWords = theInputForm.ignoreStopWords.data,
                              stemming = stemmingType)

               # display all user text if short otherwise the first fragment of it
        if len(userText) > 99:
            fragment = userText[:99] + " ..."
        else:
            fragment = userText

              # check that there is at least one unique token to avoid division by 0
        if myText.uniqueTokens() == 0:
            uniqueTokensText = 1
        else:
            uniqueTokensText = myText.uniqueTokens()

              # render the html page
        return render_template('results.html',
                           title='Text Analysis',
                           inputTypeText = typeText,
                           originalText = fragment,
                           numChars = myText.length(),
                           numSentences = myText.getSentences(),
                           numTokens = myText.getTokens(),
                           uniqueTokens = uniqueTokensText,
                           commonWords = myText.getMostCommonWords(10))
    else:
        print("11111111111111")
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(userText)
        if scores['compound'] > 0:
            sentiment='Positive'
        elif scores['compound']< 0:
            sentiment='Negative'
        else:
            sentiment='Neutral'

        return render_template('sentiment.html',
                           title='Text Analysis',
                           sentiment_scores = scores,
                           sentiment=sentiment)


  # render web form page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
      # render the initial main page
    return render_template('index.html',
                           title = 'Sentiment Analyzer',
                           form = InputTextForm())

@app.route('/results')
def results():
    return render_template('index.html',
                           title='Sentiment Analyzer')


