import spacy
import neuralcoref
# import en_core_web_sm
# nlp = en_core_web_sm.load()

nlp = spacy.load("en_core_web_md")
# nlp = spacy.load('en')


# load NeuralCoref and add it to the pipe of SpaCy's model

coref = neuralcoref.NeuralCoref(nlp.vocab)
nlp.add_pipe(coref, name='neuralcoref')

# You're done. You can now use NeuralCoref the same way you usually manipulate a SpaCy document and it's annotations.
doc = nlp(u'My sister has a dog. She loves him.')

doc._.has_coref
doc._.coref_clusters