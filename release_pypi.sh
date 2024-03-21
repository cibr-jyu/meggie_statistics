#!/bin/bash

if [[ -z "${INTERP}" ]]; then
  INTERP=python
fi

echo "Removing previous build artifacts"
rm -f dist/*

echo "Building source distribution.."
$INTERP -m build --sdist
echo "Building wheel.."
$INTERP -m build --wheel
echo "Uploading to pypi.."
$INTERP -m twine upload dist/*
echo "Finished."
