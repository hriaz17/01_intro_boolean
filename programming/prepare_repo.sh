BASEFOLDER="/Users/eduardoblanco/work/teaching/csc4583.github_repos/01_boolean_engine"
rm -rf $BASEFOLDER
mkdir -p $BASEFOLDER

cp assignment/assignment.pdf $BASEFOLDER
cp .gitignore $BASEFOLDER

for f in *.txt
do
  cp $f $BASEFOLDER
done

for f in boolean_engine.py query.py test_boolean_queries.py
do
  python prepare_python_code.py $f > $BASEFOLDER/`basename $f`
done

echo "Name: WRITE YOUR NAME HERE" > $BASEFOLDER/README.md
