# Scriptie Logboek 
## week 10: 
Whales data litaratuur onderzoek. Kijken of de data verkrijgbaar is. 

## week 11: 
Verdiepen in mempool en de literatuur hierover in combinatie met Bitcoin. 

## Week 12: 
Presentatie geven over 'scritpie onderwerp'
Literatuuronderzoek en maken van PVA. Veel papers lezen en verdiepen in onderwerp. 


## Week 13:
Ziek 

## Week 14:

### Feedback verwerken:

**Ontvangen feedback:**

About sub-question 4: The methodology section does not mention any planning to test interfaces by users. Unless you plan to validate a built prototype with actual traders or risk managers, the reliability of such an approach would be very low. In summary, you should plan this step if you are willing to build such a prototype or reduce the scope by dropping RQ4. Please discuss this with your lab supervisor, Kees van Montfort.

Research Question 6:

Ethical implications are certainly relevant, but they should be treated in the discussion section rather than framed as a separate research question. The reason is that you haven't prepared any methodological operationalisation of these concerns in your PvA, which has a very mild chance of answering such a big question.

Review Justification for Using XGBoost

The current reasoning (explainability) for choosing XGBoost is very fragile. XGBoost does provide feature importance, but that doesn't make it the only or most transparent option. Methods such as SHAP or LIME are alternatives that could also be applied to neural networks. Clarify why interpretability is necessary in this context.

Review the claim about mempool predictive power

The sentence claiming that internal blockchain variables (like mempool size) are more reliable than macroeconomic factors is an enormous oversimplification of a complex issue. Mempool data is still a proxy for complex phenomena. Please revise this claim.

Define Acronyms

Always introduce and briefly explain concepts not seen before. Examples are the mentions of IFS and PFS (you are probably referring to Fuzzy sets approaches).

Period of the Dataset

The proposal does not indicate the start and end dates of the data used. This is essential information. In which time context in which your findings apply? Is it generalisable enough across different market moments? Think of bull, bear and sideways. Please explicitly mention the temporal scope of your dataset and justify its selection.

No dataset description

No detailed description of data: There are no details about the features used or their order of magnitude. Also, there was no exploratory data analysis of the current datasets. Is it a balanced dataset regarding price movements (bearish, bullish)? If it is imbalanced, which technique are you planning to use? 

Clarify Mempool Aggregation Approach (Critical)

Since mempool data is not static, how are you aggregating it? Hourly averages? Rolling windows? Please be explicit about Frequency, Aggregates used (mean, median, standard deviation), How it's aligned with your OHLC and sentiment data

Validation Strategy Used for Time Series

Time series prediction requires validation based on time. It is not clear how you are generating your validation/test data. Yapproach? You mention splitting into validation, test, and training, but temporal data is essential here. You should not simply use a randomised split. Which approach are you using?

Reconsider Binary Classification Framing

Framing Bitcoin price prediction as a binary up/down task is extremely simplistic. More specifically, is 0,0000001 still a price up? Consider regression instead of classification or using a classification threshold to define significant" changes. The role of explainability you mentioned in the paper is unclear, and there is no mention of which technique and how it will be tested in the end.

Avoid Justification for Poor Performance even before starting

Rather than stating the model is unlikely to perform well, reframe this as an exploratory comparison of baseline vs. mempool-augmented models. That gives it a stronger academic foundation.

**Vragen over feedback:**
- Moet ik ook de verwachte resultaten feedback veranderen 
- Kan ik design gedeelte helemaal weghalen?
- Hoe splitsen? de dataset opslitsen in bear and bull market voor aparte modellen zoals in Van Waterschoot, M. (2024). To what extent do bull and bear market conditions impact the effectiveness of certain features in forecasting Bitcoin price? [Master’s thesis, Tilburg University]. Tilburg University Thesis Repository. https://arno.uvt.nl/show.cgi?fid=172279 
- Ik wil drie soorten modellen Bear - accumulation - Bull -> kan dit? 

of 1 of 2 dagen per week over de hele dataset gebruiken als validatie? (dit kan toch niet, want ik kijk naar de afgelopen 30 dagen)

- - is het aggregreren van de mempool data + holc data goed? 

- Baseline model selection -> Nu wel goed verantwoord waarom XGboost? Is de argumentatie beperkte rekenkracht en bewezen goede prestaties goed genoeg? OOk het doel is niet om een zo goed mogelijk model te maken, maar te vergelijken met baseline dus efficientie en goed is van belang. 
- Heb ik op een goede manier een derde optie toegevoegd: omlaag - neutraal - omhoog. waardoor het niet meer binair is maar een meerdere klasse probleem. 

- Ik kan niet rolling window validation doen want de prijs bevat informatie ove toekomst. Door te splitsen op cycle en dan laatste 20% is meest betrouwbaar omdat hier geen data leakage is. Maar dit is wel dan eenzeidig want het is een vaste fase (eind fase bull/bear/accumulatie)



**Antwoorden van Meeting Marcio//Boris:**
