import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5*math.log((1-p)/p)"

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.527
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan's decision to use coin flipping is ineffective because it purely relies on chance and excludes valuable market insights. Ensemble methods enhance accuracy by pooling results from multiple models, each of which consistently outperforms the probabilistic nature of coin flipping."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "C2 is not an improvement over C1, as both classifiers achieve the same expected rates of true and false positives, placing them directly on the line of random guessing on the ROC curve and reflecting their lack of effective predictive power"

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "In this particular scenario, precision and recall are the key metrics, assessing the balance of true positive predictions (precision) and the model's effectiveness in identifying all positives (recall). As C2 has a higher recall than C1, it could arguably be considered a better classifier when using these metrics"
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 is a superior classifier to C1 because it achieves a much higher recall/TPR and F1-measure, showing that it not only identifies more positive cases accurately but also better manages the balance between precision and recall."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "For imbalanced datasets with fewer positive cases, precision, recall, and F1-measure are indispensable metrics, as they deliver a holistic view of the classifier’s performance and capabilities"

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C2"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C2 is more desirable because it strikes the best balance between precision and recall, as shown by its highest F1-measure. C3, although it leads in precision, lacks in recall, which is a disadvantage in applications where finding all positive cases is pivotal"
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "p"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "2 * (0.1 * p) / (0.1 + p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
    'recall': 0.5333,
    'precision': 0.6154,
    'F-measure': 0.5714,
    'accuracy': 0.88
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "The F-measure is the ideal metric in cases like this, where precision and recall need to be balanced, particularly in imbalanced class scenarios such as predicting weather outcomes, where one type might dominate. Accuracy is the least useful metric because it can be high due to a large number of true negatives and does not truly indicate the model’s effectiveness in predicting minority class outcomes"
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "When the substantial risks associated with missing a diagnosis (false negatives) outweigh those related to false positives, TPR/FPR stands out as the most effective measure for evaluating cancer tests T1 and T2. It highlights the tests' proficiency in correctly spotting genuine positives"

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "If there is a low probability of cancer in the population being tested, the F-measure becomes more critical than TPR/FPR. False positives can lead to psychological discomfort, dangerous follow-up tests, and increased treatment costs. The F-measure, which accounts for both true and false positives, should be prioritized to enhance precision and reduce these negative effects, particularly when subsequent procedures following a positive result are expensive and hazardous."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
