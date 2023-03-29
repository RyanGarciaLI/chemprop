python predict.py \
    --test_path ../antibiotics/test_ecoli_antibiotics.csv \
    --preds_path ../checkpoints/ecoli_20iter_feat_110_001_B/train_20folds_1ensem_class_2/predict_ecoli_antibiotics_one_class \
    --checkpoint_dir ../checkpoints/ecoli_20iter_feat_110_001_B/train_20folds_1ensem_class_2 \
    --config_path ../checkpoints/config_official.json \
    --features_generator rdkit_2d_normalized --no_features_scaling