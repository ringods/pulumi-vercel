// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vercel.Outputs
{

    [OutputType]
    public sealed class DnsRecordSrv
    {
        public readonly int Port;
        public readonly int Priority;
        public readonly string Target;
        public readonly int Weight;

        [OutputConstructor]
        private DnsRecordSrv(
            int port,

            int priority,

            string target,

            int weight)
        {
            Port = port;
            Priority = priority;
            Target = target;
            Weight = weight;
        }
    }
}
