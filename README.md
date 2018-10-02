# RU_BE
Glossary and transliteration rules for RU->BE

The following resources are meant to be used for a project on Neural Machine Translation for low-resource languages. 
The method should be easily applied to other low-resource languages with minimum adjustments, this is why the degree of refinement required for the following tasks is very low. We do not perform any lemmatisation or stemming, since these resources are not available for all languages. For practical reasons, human effort should also be limited.

# ru_be_dict.py
Glossary of the 200 most frequent Russian words, translated into Belorussian.

# translit_it_es.py
Example transliteration rules (IT->ES) used in the experiments mentioned in the NAACL paper "Using Related Languages to Enhance Statistical Language Models" (Currey and Karakanta, 2016).

# translit_ru_be.py
Transliteration rules for Russian characters and character combinations that are not present in Belorussian. They are less   detailed than the transliteration rules in the IT->ES file above. This was used for the research in "Neural Machine Translation for Low-Resource Languages without Parallel Data" (Karakanta et al., 2018).
