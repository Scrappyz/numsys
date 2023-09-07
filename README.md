## numsys
A python program to operate on numbers systems.

<!-- omit in toc -->
## Table Of Contents
- [numsys](#numsys)
- [Usage](#usage)

## Usage
### Convertion
```
numsys convert [option] <input> <from_base> <to_base>
```

Use the `convert` subcommand to convert an input to another base number system.

#### Example 
```
numsys convert 29 10 2
```

In this example, our input is `29` and we want to convert `29` from base 10 (decimal) to base 2 (binary).

##### Output
```
11101
```
<br>
It is also possible to show the solution of how the convertion process is done by adding the `-s` or `--solution` flag.

```
numsys convert 29 10 2 -s
```

##### Output
```
29/2 = 14 r 1
14/2 = 7 r 0
7/2 = 3 r 1
3/2 = 1 r 1
1/2 = 0 r 1
11101
```