interface StatCardProps {
  label: string
  value: number | string
  color?: string
}

export default function StatCard({ label, value, color = 'var(--color-primary)' }: StatCardProps) {
  return (
    <div style={styles.card}>
      <span style={{ ...styles.value, color }}>{value}</span>
      <span style={styles.label}>{label}</span>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  card: {
    background: 'var(--color-surface)',
    border: '1px solid var(--color-border)',
    borderRadius: 'var(--radius)',
    padding: '1.5rem',
    display: 'flex',
    flexDirection: 'column',
    gap: '0.5rem',
    boxShadow: 'var(--shadow)',
  },
  value: { fontSize: '2rem', fontWeight: 700 },
  label: { fontSize: '0.875rem', color: 'var(--color-muted)' },
}
