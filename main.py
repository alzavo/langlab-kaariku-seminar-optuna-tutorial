import optuna
from optuna import Trial


def suggest_parameters():
    pass


def create_job_command():
    pass


def get_metrics():
    pass


def objective(trial: Trial):
    suggest_parameters()
    create_job_command()
    # run command as a subprocess
    # capture the srun job id, name or something to identify
    get_metrics()
    # check if pruner should finish this trial
    # prune if necessary
    # kill the job on the cluster
    # clean the models checkpoints or other files which can take much space
    return None


if __name__ == "__main__":
    STUDY_NAME = "nocasa"
    DIRECTION = "maximize"

    SAMPLER = optuna.samplers.TPESampler(multivariate=True)
    PRUNER = optuna.pruners.HyperbandPruner()
    
    STORAGE = optuna.storages.JournalStorage(
        optuna.storages.journal.JournalFileBackend(f"study.journal")
    )

    study = optuna.create_study(
        study_name=STUDY_NAME,
        storage=STORAGE,
        direction=DIRECTION,
        sampler=SAMPLER,
        pruner=PRUNER,
        load_if_exists=True
    )
    study.optimize(objective, n_trials=30)
