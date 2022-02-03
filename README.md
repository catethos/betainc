# README

I attempt to compile the same c code using `cython` and `emscripten` so that the same code can be used as python extension and web assembly in the browser.

## Python
You can install the c-extension using poetry
```
poetry install
```

## Javascript
Precompiled `.wasm` file is in the `webassembly` folder. Please look `script.js` to see how to import the web assembly file to the browser.