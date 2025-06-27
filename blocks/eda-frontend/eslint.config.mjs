// eslint.config.mjs
import babelParser from '@babel/eslint-parser'
import js from '@eslint/js'
import importPlugin from 'eslint-plugin-import'
import nPlugin from 'eslint-plugin-n'
import promisePlugin from 'eslint-plugin-promise'
import reactPlugin from 'eslint-plugin-react'
import reactHooksPlugin from 'eslint-plugin-react-hooks'
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
        ecmaVersion: 2022,
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
      'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],

      // React/React Hooks
      'react/jsx-uses-vars': 'error',
      'react/react-in-jsx-scope': 'off',
      'react-hooks/exhaustive-deps': 'warn',
      'react-hooks/rules-of-hooks': 'error',

      // Import order
      'import/order': ['warn', {
        groups: [
          'builtin',
          'external',
          'internal',
          'parent',
          'sibling',
          'index',
          'object',
          'type'
        ],
        pathGroups: [
          {
            pattern: '{react,react-dom,react-loader-spinner,react-redux,react-router-dom}',
            group: 'external',
            position: 'before'
          },
          {
            pattern: '{@material-ui/**,@mui/**}',
            group: 'external',
            position: 'after'
          }
        ],
        pathGroupsExcludedImportTypes: ['builtin'],
        'newlines-between': 'always',
        alphabetize: {
          order: 'asc',
          caseInsensitive: true
        }
      }]
    }
  }
]
