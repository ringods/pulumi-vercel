// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel.Outputs
{

    [OutputType]
    public sealed class FirewallConfigRulesRuleActionRedirect
    {
        public readonly string Location;
        public readonly bool Permanent;

        [OutputConstructor]
        private FirewallConfigRulesRuleActionRedirect(
            string location,

            bool permanent)
        {
            Location = location;
            Permanent = permanent;
        }
    }
}
