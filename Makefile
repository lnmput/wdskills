.PHONY: update status sync validate test

update:
	@node scripts/manage-skills.mjs update

status:
	@node scripts/manage-skills.mjs status

sync:
	@node scripts/manage-skills.mjs sync

validate:
	@node scripts/manage-skills.mjs validate

test:
	@node scripts/manage-skills.mjs test
