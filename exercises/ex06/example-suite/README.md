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

### Viewing the output graph

You can view the output graph with this command:

```
display $HOME/cylc-run/workshop-suite/outputs/annual-max-temp-time-series.png
```
