# Chaii
kaggle「chaii - Hindi and Tamil Question Answering」コンペにて使用したモデルなどを格納しています。

# modelフォルダ内の各model解説 
①eaw-hinge-reinit3-l3<br>
lovasz-hinge損失を活用したマルチタスク訓練&roberta-encoder最終３層の重みを初期化&roberta-encoder最終３層をconcatして出力実行<br>
publicLB/privateLB：0.774/0.721<br>
<br>
②eaw-reinit2-msd<br>
roberta-encoder最終2層の重みを初期化&マルチサンプルドロップアウト<br>
publicLB/privateLB：0.774/0.737<br>
<br>
③external-answer-weight-last3<br> 
roberta-encoder最終３層をconcatして出力実行<br> 
publicLB/privateLB：0.774/0.741（最終銀メダル圏内）<br>
<br>
④external-answer-weight<br>
10fold&サンプルの性質によって重みが変わる、cross_entropyを使用<br> 
publicLB0.787の元モデル<br> 
publicLB0.787のモデルはこのモデルのfold1,2,3,4,10をアンサンブルして作成<br>
publicLB/privateLB：0.787/0.729<br>
