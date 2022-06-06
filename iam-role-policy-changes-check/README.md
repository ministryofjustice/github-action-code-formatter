# iam-role-policy-changes-check

This GH Action is used within Pull requests (PRs) on the [MoJ Cloud Platform][cloud-platform], changes have to be approved by the Cloud Platform team.

This Github Action marks PRs as failed if they contain content that is related IAM and IAM policies.

## USAGE

Create a file in your repo called `.github/workflows/iam-role-policy-changes-check.yml` with the
following contents:

```
name: Identify PRs that contain IAM Role and Policy changes

on:
  pull_request

env:
  PR_OWNER: ${{ github.event.pull_request.user.login }}
  GITHUB_OAUTH_TOKEN: ${{ secrets.DOCUMENT_REVIEW_GITHUB }}

jobs:
  check-diff:
    runs-on: ${{ matrix.os }}

    strategy:
      matrix:
        os: [ubuntu-latest]

    steps:
      - name: Checkout PR code
        uses: actions/checkout@v3
      - run: |
          git fetch --no-tags --prune --depth=1 origin +refs/heads/*:refs/remotes/origin/*
      - name: Run git diff against repository
        run: |
          git diff origin/main HEAD > changes
      - name: Run iam/role policy changes check
        id: review_pr
        uses: ministryofjustice/github-actions/iam-role-policy-changes-check@main
      - name: Request changes in the PR
        uses: andrewmusgrave/automatic-pull-request-review@0.0.5
        if: steps.review_pr.outputs.review_pr_iam_check == 'false'
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN  }}"
          event: COMMENT
          body: |
            There are potential IAM Role and/or policy Changes/additions. Reviewer - If satisfied with the changes/additions - dismiss this request
```

`secrets.DOCUMENT_REVIEW_GITHUB` needs to be provided.

[cloud-platform]: https://github.com/ministryofjustice/cloud-platform
