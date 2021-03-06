import nltk 
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser
from nltk.corpus import verbnet as vn
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
from nltk.corpus import framenet as fn
from pprint import pprint
from awesome_print import ap 

parser = load_parser('NewGrammar.fcfg')


run_senses = {'meander-47.7': 'figurative', 
'preparing-26.3-1':'figurative',
'run-51.3.2': 'literal',
'swarm-47.5.1-1': 'figurative'
}

def isFigurativeLanguage(test):
	lambdaExpressions = [tree.label()['SEM'] for tree in parser.parse(test.split())]
	
	predicates = [predicate.name for expression in lambdaExpressions
								 for predicate in expression.predicates()]


	verbs = {verb:lesk(test,verb,'v') for verb in predicates}


	for word,pos in nltk.pos_tag(nltk.word_tokenize(test)):
		if 'N' in pos or 'V' in pos:
			lexical_units =  fn.lus(r'(?i)%s.%s'%(word,pos.lower()[0]))
			for lu in lexical_units:
				print lu.definition
	'''
		Figurative Language:
		  1. Some verbs are used only figuratively
		  2. Some verbs are used more frequently or most frequently in figurative sense

		  A sentence is figurative if:
			1. All of the verbs in the sentence belong to (1)
			2. All of the verbs in the sentence belong to (1) or belong to (2) and are 
			   being used in a figurative sense

		 A verb that can be used in a concrete or figurative sense is being used in a figurative
		 sense when the subjects or objects of the verb are:
			(1) abstract nouns
			(2) concrete 

	'''


metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 

'''
for tree in parser.parse(metaphor1.split()):
	lambdaexpression = (tree.label()['SEM'])
print(lambdaexpression)


parsed = lambdaexpression
predicates_from_parsed =[]
swag =[]
verbs=[]

for p in parsed.predicates():
	print(p)
	swag.append(p)
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
	initial = metaphor1.split
	if 'V' in pos: #Another way to focus on only verbs
			verbs.append(word)
print(verbs)
print(nltk.pos_tag(nltk.word_tokenize(metaphor1)))
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
	print (word,'\t')
	if "N" in pos:
		pos = "n"
	if "V" in pos:
		pos = "v"
	print (lesk(metaphor1, word, pos))## Trying to use for sense identification

for word in verbs:
	final = [sense for sense in vn.classids(word)]
	print (final)
	for sense in final:
		x = vn.lemmas(sense)
		print (x)
		#for thing in x:
		#   print (fn.lus(r'(?i)%s'%(x)))

for x in final:
	print(run_senses[x])


for x in nltk.word_tokenize(metaphor1):
	print (fn.lus(r'(?i)%s'%(x)))
print (fn.lus('race'))
'''

print(fn.frames_by_lemma(r'(?i)run'))
print(fn.frames_by_lemma(r'(?i)race'))

run_frames = (fn.frames_by_lemma(r'(?i)run'))
race_frames = (fn.frames_by_lemma(r'(?i)race'))

for frame1 in run_frames:
    for frame2 in race_frames:
        if frame1==frame2:
            print ("Progress")
            #attempting to see if frames of the two have any correlation
    
##print (fn.fes('Noise_maker'))
##Has error AttributeError: 'FramenetCorpusReader' object has no attribute 'fes'

print (fn.lu_ids_and_names("run"))
print (fn.lu_ids_and_names("race")) #use to determine which LU to use
>>>>>>> upstream/master
