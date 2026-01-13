# Running the workflow

## To run the workflow

`cylc install`
`cylc play`

## To stop the workflow (if failed/still running)

`cylc stop workshop-workflow`

## To clean out the workflow working directory

`cylc clean workshop-workflow`

This can be required before re-running.

## Working directory

When Cylc runs the workflow it has a working directory where the workflow is run.
This is referenced in the `flow.cylc` file with the environment variable
`$CYLC_WORKFLOW_RUN_DIR`.

By default this will be under:

```
$HOME/cylc-run/<workflow_name>/
```

### Working directory for Workshop example workflow

In the case of the `workshop-workflow` the working directory will be:

```
$HOME/cylc-run/workshop-workflow/
```

The workshop workflow uses this as the common location for all scripts and the outputs
directory to be located in. 

The final output graph is written to:

```
$HOME/cylc-run/workshop-workflow/runN/outputs/annual-max-temp-time-series.png
```

### View the final time series graph of maximum temperatures

You can view the output graph with this command (`display` command is only available on login-0? and sci-vm-0? servers, not the cylc2.jasmin.ac.uk):

```
display $HOME/cylc-run/workshop-workflow/runN/outputs/annual-max-temp-time-series.png
```

## Additional Cylc commands

### Stopping a workflow that is running

Note: In our example workflow, named 'workshop-workflow', you would change the value of '<WORKFLOW>' to
'workshop-workflow' in the following commands.

If you need to stop the workflow you can use:

```
cylc stop '<WORKFLOW>'
```

The `cylc stop` command may not stop the workflow immediately - because it will wait for submitted
and running tasks to complete.

To kill the submitted and running tasks before stopping the workflow, use:

```
cylc stop --kill '<WORKFLOW>'
```

To stop the workflow regardless of submitted and running tasks (shut down immediately, leave active tasks alone), use:

```
cylc stop --now '<WORKFLOW>'
```

### Viewing the workflow graph of the workflow

To view the workflow graph of your workflow _without_ running it, use:

```
cylc install
cylc graph workshop-workflow
```

NOTE: the `cylc install` only installs the workflow - so this will not run the workflow until `cylc play` is run.


### Viewing available platform options on the system

```
cylc config --platforms
```

This will list the options you have available that you can use in your `flow.cylc` file - such as running on the local system, or on lotus, e.g.:

```
$ cylc config --platforms
[platforms]
    [[localhost]]
        install target = localhost
        copyable environment variables = FCM_VERSION
        submission polling intervals = PT30M
        execution polling intervals = PT30M
        execution time limit polling intervals = PT5M, PT10M
        clean job submission environment = True
    [[lotus]]
        install target = localhost
        copyable environment variables = FCM_VERSION
        submission polling intervals = PT30M
        execution polling intervals = PT30M
        execution time limit polling intervals = PT5M, PT10M
        clean job submission environment = True
        hosts = localhost
        job runner = slurm
        [[[meta]]]
            description = LOTUS Slurm job
```
