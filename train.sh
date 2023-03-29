python train.py \
  --dataset_type classification \
  --data_path ../antibiotics/ecoli_scaffold/train_val.csv \
  --separate_test_path ../antibiotics/ecoli_scaffold/test.csv \
  --config_path ../checkpoints/ecoli_20iter_feat_110_001_U_3D/hyopt_1ensem_no_class/config_U_3D.json \
  --save_dir ../checkpoints/ecoli_20iter_feat_110_001_U_3D/train_20folds_1ensem_no_class_7depth \
  --epochs 30 \
  --ensemble_size 1 \
  --save_smiles_splits \
  --num_folds 20 \
  --features_generator rdkit_2d_normalized --no_features_scaling \
  --save_preds \
  --extra_metrics prc-auc \
  --depth 7