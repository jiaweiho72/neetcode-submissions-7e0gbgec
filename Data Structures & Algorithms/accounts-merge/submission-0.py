class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        DSU (stores the index in account)
        - get the 'parent' as in the representative account
            - every account starts off as itself as parent

        - email_to_account:
            get the last account instantly based on a common email
            - union if you see the same email, union to the account

        once done, go through all accounts again

        result must be sorted
        """
        
        n = len(accounts)

        # 1) DSU init
        parent = list(range(n)) # 0, 1, 2 ... maps representing index in account
        size = [1] * n
        def find(x):
            while parent[x] != x: # while not itself -> not the root yet
                parent[x] = parent[parent[x]] # path compression
                x = parent[x] # move upwards
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: # if parents same -> already in same component -> do nothing
                return 
            if size[ra] < size[rb]: # short one hang onto long one
                parent[ra] = rb
                size[rb] += size[ra]
            else:
                parent[rb] = ra
                size[ra] += size[rb]
        
        # 2) Discover common email connections, mark first-seen emails
        email_to_acct = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acct: # if common email -> union and group tgt
                    union(i, email_to_acct[email])
                else: # else is a first-seen email, not that down
                    email_to_acct[email] = i

        # 3) Format the output: person + emails
        """
        have a dict root_to_emails
        iterate every account, and insert into the root parent the emails. To ensure no duplicates, the emails should be a set.

        since, all under the same component will have the same name, the result is straightforward
        """

        root_to_emails = defaultdict(set)
        for i, account in enumerate(accounts):
            cur_root = find(i)
            root_to_emails[cur_root].update(account[1:]) # update all emails to this root
        
        result = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0] # all accounts in the same group has same name
            result.append([name] + sorted(emails)) # emails set converted to a sorted list

        return result


            










