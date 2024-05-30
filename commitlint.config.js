module.exports = {
	extends: ['@commitlint/config-conventional'],
	rules: {
		// Here you can add custom rules or override the default ones
		'type-enum': [
			2,
			'always',
			[
				'feat', // new feature
				'fix', // bug fix
				'docs', // documentation only changes
				'style', // formatting, missing semi colons, etc; no code change
				'refactor', // refactoring production code
				'test', // adding tests, refactoring test; no production code change
				'chore', // updating grunt tasks etc; no production code change
			],
		],
		// You can also specify the scopes you use
		'scope-enum': [
			2,
			'always',
			[
				'auth', // authentication related changes
				'api', // API related changes
				'models', // database models changes
				'views', // frontend views changes
				'utils', // utility functions and helpers
				// Add more scopes here
			],
		],
		// Other rules...
	},
};
