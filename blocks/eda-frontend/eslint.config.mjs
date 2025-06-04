// eslint.config.js
import js from '@eslint/js'
import babelParser from '@babel/eslint-parser'
import reactPlugin from 'eslint-plugin-react'
import reactHooksPlugin from 'eslint-plugin-react-hooks'
import importPlugin from 'eslint-plugin-import'
import nPlugin from 'eslint-plugin-n'
import promisePlugin from 'eslint-plugin-promise'
import globals from 'globals'

export default [
  js.configs.recommended,

  {
    languageOptions: {
      parser: babelParser,
      parserOptions: {
        requireConfigFile: false,
        babelOptions: {
          presets: [
            ['@babel/preset-react', { runtime: 'automatic' }]
          ]
        },
        ecmaFeatures: {
          jsx: true
        },
        ecmaVersion: 2018,
        sourceType: 'module'
      },
      globals: {
        ...globals.browser,
        ...globals.node
      }
    },

    linterOptions: {
      reportUnusedDisableDirectives: true
    },

    plugins: {
      react: reactPlugin,
      'react-hooks': reactHooksPlugin,
      import: importPlugin,
      n: nPlugin,
      promise: promisePlugin
    },

    settings: {
      node: {
        version: '>=18.0.0'
      },
      react: {
        version: 'detect'
      }
    },

    rules: {
      // Style rules
      'space-before-function-paren': ['error', 'always'],
      semi: ['error', 'never'],
      quotes: ['error', 'single'],
      'comma-dangle': ['error', 'never'],
      indent: ['error', 2],
      'no-var': 'error',
      'prefer-const': 'error',

      // React/React Hooks
      'react/jsx-uses-vars': 'error',
      'react/react-in-jsx-scope': 'off',
      'react-hooks/exhaustive-deps': 'warn',
      'react-hooks/rules-of-hooks': 'error'
    }
  }
]
