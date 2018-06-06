from filecmp import cmp

fnames = ['results/naive_bayes', 'results/svm_estimator']
for f in fnames:
    true_or_false = str(cmp(f+'_original.png', f+'.png')).lower()
    print('[{}] {} is equal.'.format(true_or_false, f))
