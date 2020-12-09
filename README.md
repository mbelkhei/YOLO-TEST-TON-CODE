# Instructions

#### Getting started:

1. Clone repo: `git clone ssh://git@bitbucket.f.bbg:7999/b9c3-big-data_datascience-bpce-sa/yolo-test-ton-code.git`
2. placez vous dans le repertoire parent : ***yolo-test-ton-code***
3. Assurez vous que vous êtes sur la branch ***master*** (`git checkout master`)
4. Creéz votre environment conda avec la commande
   `bash >>> ./conda_script.sh
`
5. Vous devez taper le dossier où se trouve votre Anaconda3. Example: `/d/donnees/belkheir/appdata`
6. Le message "Your conda environment is ready to be used" vous indique que votre environment est prêt
7. Dans votre bash git, activez votre environement conda: `conda activate yolo_test_env`
8. `(yolo_test_env)>>>$`
9. Mettez vous sur votre branch (ie: `git checkout -b groupe1 origin/groupe-1`)
10. vous êtes prêts !



#### contraintes: 
- **context** : Python
- **Abstraction de classe** : chaque class de transformer doit contenir les méthodes suivants:
    - my_transformer_fit = mytransformer.fit(X_train)
    - mytransformer_fit.transform(X_train), mytransformer_fit.transform(X_test)
    - mytransformer.fit_transform(X_train)
    >You can use the fit_transform() method on the training set, as you’ll need to both fit and transform the data, and you can use the fit() method on the training dataset to get the value, and later transform() test data with it"
- **Documentation** : 
  - décrire le comportement de la classe et de ses méthodes (si besoin) avec une ou deux phrases
  - >Remarque: il y a déjà une phrase qui décrit le comportement de chaque transformer, vous pouvez la modifier a votre sauce
  - donner un exemple de démonstration (simple)
- **Commit**: chaque groupe fait un seul commit chaque 15 min


#### Requirements:

- Git
- Gitbash
- Data: le jeux de données se trouve dans **YOLO-TEST-TON-CODE/data**
- Lib :
    - pytest
    - numpy
    - pandas
    - scikit-learn
