
# Instructions

#### Getting started:

1. Clone repo: git clone https://github.com/mbelkhei/YOLO-TEST-TON-CODE.git
2. placez vous dans le repertoire parent : ***yolo-test-ton-code***
3. Assurez vous que vous êtes sur la branch ***master*** (`git checkout master`)
4. Creéz votre environment conda avec la commande
   `bash >>> ./condaenv.sh`
5. Indiquez le dossier où se trouve votre Anaconda3. Example: `/d/donnees/belkheir/appdata`
6. Le message **"Activating your yolo_test_env"** vous indique que votre environment est prêt
7. `(yolo_test_env)>>>$`
8. Mettez vous sur votre branch (ie: `(yolo_test_env)>>>git checkout -b groupe-1 origin/groupe-1`)
9. Utilisez la commande `git branch -vv` pour verifier que les branches `master` et `votregroupe` suivent les branches `origin/master` et `origin/votregroupe` respectivement 
10. Vous êtes prêts à tester votre code ;)



#### Contraintes: 
- **Context** : Python
- **Abstraction de classe** : chaque class de transformer doit contenir les méthodes suivants:
    - my_transformer_fit = mytransformer.fit(X_train)
    - mytransformer_fit.transform(X_train), mytransformer_fit.transform(X_test)
    - mytransformer.fit_transform(X_train)
    >You can use the fit_transform() method on the training set, as you’ll need to both fit and transform the data, and you can use the fit() method on the training dataset to get the value, and later transform() test data with it"
- **Documentation** : 
  - Décrire le comportement de la classe et de ses méthodes (si besoin) avec une ou deux phrases
  - >Remarque: Il y a déjà une phrase qui décrit le comportement de chaque transformer, vous pouvez la modifier a votre sauce
  - Ajoutez un exemple de démonstration (simple) dans le tag `[ADD EXAMPLE]`
- **Commit**: Chaque groupe fait un seul commit chaque 15 min


#### Requirements:

- Git
- Gitbash
- Data: le jeux de données se trouve dans **YOLO-TEST-TON-CODE/data**
- Lib :
    - pytest
    - numpy
    - pandas
    - scikit-learn
