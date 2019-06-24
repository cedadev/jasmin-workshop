# Running the suite

## To run the suite

`rose suite-run`

## To stop the suite (if failed/still running)

`cylc stop 'example-suite'`

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

### Stopping a suite that is running

If you need to stop the suite you can use:

```
cylc stop 'example-suite'
```

### Working directory for the example suite

In the case of the `example-suite` the working directory will be:

```
$HOME/cylc-run/example-suite/
```

The example suite uses this as the common location for all scripts and the outputs
directory to be located in. 

### Viewing the workflow graph of the suite

To view the workflow graph of your suite _without_ running it, use:

```
rose suite-run -i
cylc graph example-suite
```

NOTE: the `-i` option means "install only" - so this will not run the suite.
