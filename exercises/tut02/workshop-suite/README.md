# Running the suite

## To run the suite

`rose suite-run`

## To stop the suite (if failed/still running)

`cylc stop 'workshop-suite'`

## To clean out the suite working directory

`rose suite-clean --yes`

This can be required before re-running.

Alternatively, you can force clean-up and re-run the suite with one command:

`rose suite-run --new`

## Working directory

When Cylc runs the suite it has a working directory where the suite is run.
This is referenced in the `suite.rc` file with the environment variable
`$CYLC_SUITE_RUN_DIR`. 

By default this will be under:

```
$HOME/cylc-run/<suite_name>/
```

### Working directory for Workshop example suite

In the case of the `workshop-suite` the working directory will be:

```
$HOME/cylc-run/workshop-suite/
```

The workshop suite uses this as the common location for all scripts and the outputs
directory to be located in. 

The final output graph is written to:

```
$HOME/cylc-run/workshop-suite/outputs/annual-max-temp-time-series.png
```

### View the final time series graph of maximum temperatures

You can view the output graph with this command:

```
display $HOME/cylc-run/workshop-suite/outputs/annual-max-temp-time-series.png
```

## Additional Rose & Cylc commands

### Stopping a suite that is running

Note: In our example suite, named 'example-suite', you would change the value of '<SUITE>' to
'example-suite' in the following commands.

If you need to stop the suite you can use:

```
cylc stop '<SUITE>'
```

The `cylc stop` command may not stop the suite immediately - because it will wait for submitted
and running tasks to complete.

To kill the submitted and running tasks before stopping the suite, use:

```
cylc stop --kill '<SUITE>'
```

To stop the suite regardless of submitted and running tasks, use:

```
cylc stop --now '<SUITE>'
```

### Viewing the workflow graph of the suite

To view the workflow graph of your suite _without_ running it, use:

```
rose suite-run -i
cylc graph example-suite
```

NOTE: the `-i` option means "install only" - so this will not run the suite.


